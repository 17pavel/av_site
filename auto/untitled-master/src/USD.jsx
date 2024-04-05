

    const r = require('unirest');
    const ch = require('cheerio');
    let usd_current = ''
    let usd = Number
    function USD() {
    return (r.get('https://myfin.by/bank/kursy_valjut_nbrb/usd').end(function (response) {
            const body = response.body;
            const $ = ch.load(body);
            const usd_pars = $('.h1 ').text();
            for (let i = 0; i < (usd_pars.length / 2); i++) {
                usd_current = usd_current + usd_pars[i];
            }
            usd = Number(usd_current);
            return (usd)

                    }))}

let m = USD()
console.log(m.usd)



