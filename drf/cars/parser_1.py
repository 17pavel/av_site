import requests
from bs4 import BeautifulSoup
from tqdm import tqdm
import json
from dataclasses import dataclass, field
from items.models import Products, Images, Categories


@dataclass(slots=True)
class Kufar:
    name: str = field(default="")
    price: float = field(default=0.0)
    slug: str = field(default="")
    quantity: int = field(default="1")
    discount: float = field(default=0.0)
    url: str = field(default="")
    description: str = field(default="")
    parameter: dict = field(default_factory=dict)
    images: list = field(default_factory=list)

    def __eq__(self, other):
        if isinstance(other, Kufar):
            return self.url == other.url


URL = "https://api.kufar.by/search-api/v2/search/rendered-paginated"
CURSOR = "eyJ0IjoiYWJzIiwiZiI6dHJ1ZSwicCI6MX0="
CAT = "16040"


class Parser_kufar:
    HEADERS = {
        "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
        "accept-language": "ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7",
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36",
    }

    def __init__(self, id, cat, name):
        self.cat = cat
        self.name = name
        self.id = id
        # self.slug = slug

    @classmethod
    def get_soup(cls, url: str) -> BeautifulSoup:
        response = requests.get(url, headers=cls.HEADERS)
        print(f"{response.status_code} | {url}")
        soup = BeautifulSoup(response.text, "lxml")
        return soup

    def get_json(self, cursor) -> str:
        params = {
            "cat": self.cat,
            "cursor": cursor,
            "lang": "ru",
            "size": "200",
        }
        r = requests.get(
            url=URL,
            params=params,
            headers=self.HEADERS,
        )
        data = json.loads(r.text)
        #        with open("kufar.json",  "w",  encoding="utf-8") as f:
        #            f.write(json.dumps(data, ensure_ascii=False,  indent=4))
        return data

    def get_data(self) -> list:
        items = []
        cursor = CURSOR
        while True:
            data = self.get_json(cursor)
            for el in data["ads"]:
                item = Kufar()
                try:
                    item.name = el["subject"]
                    item.slug = el["ad_id"]
                    item.url = el["ad_link"]
                    item.price = int(el["price_usd"]) / 100
                    item.images = [
                        f"https://rms8.kufar.by/v1/gallery/{i['path']}"
                        for i in el["images"]
                    ]
                    item.description = f"{item.name} | {item.price}"
                    parameters = el["ad_parameters"]

                    item.parameter = {}
                    for el in parameters:
                        item.parameter[el["pl"]] = el["vl"]

                except KeyError:
                    pass
                if item not in items:
                    items.append(item)
            print(len(items), items.__sizeof__())
            for el in data["pagination"]["pages"]:
                if el["label"] == "next":
                    cursor = el["token"]
            if not data["pagination"]["pages"][-1]["token"]:
                break
            break
        try:
            items=self.get_descr(items)
            self.save(items)
        except Exception as e:
            print(e)

        return items

    def get_descr(self, data: list) -> list:
        for el in tqdm(data):
            soup = self.get_soup(el.url)
            try:
                descr = soup.find("div", itemprop="description").text
                el.description = descr
            except (KeyError, AttributeError):
                pass

        return data

    def save(self, data: list) -> None:
        products_instances = []
        images_instances = []
        category = self.id
        # category = Categories.objects.create(
        #     name=self.name, slug=self.slug, pk=self.cat
        # )
        for product in data:
            product_instance = Products.objects.create(
                name=product.name,
                url=product.url,
                slug=product.slug,
                description=product.description,
                parameter=product.parameter,
                discount=product.discount,
                quantity=product.quantity,
                price=product.price,
                category_id=category,
            )
            for img in product.images:
                image_instance = Images.objects.create(
                    image=img, product_id=product_instance.pk
                )
                images_instances.append(image_instance)

            products_instances.append(product_instance)

        Products.objects.bulk_create(products_instances)
        Images.objects.bulk_create(images_instances)
        print("Ok")


# notebook = Parser_kufar("16040", "Ноутбуки", "notebooki")
# planshet = Parser_kufar("17050", "Планшеты", "plansheti")
# telephon = Parser_kufar("17010", "Телефоны", "telephoni")
# ebook = Parser_kufar("17070", "Электронные книги", "electronnye_knigi")
# cars = Parser_kufar("2010", "Легковые авто", "cars")
# cars = Parser_kufar("2030", "Мотоциклы", "moto")
# cars = Parser_kufar("2090", "Спецтехника", "spectech")
# cars = Parser_kufar("2060", "Грузовики", "trucs")
# cars = Parser_kufar("2075", "Шины", "tyres")
# data = cars.get_data()
# cars.get_descr(data)
# cars.save(data)
