import './App.css';
import Tyt from "./AV";
import AVMenu from "./AV-menu";
import AVContent from "./AV-content";
import React, {useState} from "react";


export const SelectContex = React.createContext()
export default function Main() {
         const [se, setSe] = useState();
        const [ty,setTy] = useState();
    const s1 = (s) => setSe(s);
    const t1 = (t) =>setTy(t);
    return(
        <>
            <SelectContex.Provider value={{s1, t1}}>
        <Tyt/>
        <AVMenu/>
        <AVContent se={se} ty={ty}/>
            </SelectContex.Provider>
        </>
    )
}