import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import axios from "axios";
import { toast } from "react-toastify";




export default function House2(props) {


    const navigate = useNavigate();
    //REgister Form 
    const [formHouse2, setFormHouse2] = useState({
        img_url: "",
        img_url2: ""

    });

    const onChangeForm = (label, event) => {
        switch (label) {
            case "img_url":
                setFormHouse2({ ...formHouse2, img_url: event.target.value });
                break;
            case "img_url2":
                setFormHouse2({ ...formHouse2, img_url2: event.target.value });
                break;
            
        }


    }

    const onSubmitHandler = async (event) => {
        event.preventDefault()
        console.log(formHouse)

        await axios.post("http://127.0.0.1:8000/houses/create-house/", formHouse)
            .then((response) => {

                navigate("/?signin");

                toast.success(response.data.detail);

                setTimeout(() => {
                    window.location.reload();
                }, 1000);

                console.log(response);
            })
            .catch((error) => {
                console.log(error);

                toast.error(error.response.data.detail);
            });

    };
    return (
        <React.Fragment>
            <div>
                <h1 className="text-3x1 font-bold text-center mb-4 cursor-pointer">
                    List your Property
                </h1>
                <p className="w-80 text-center text-sm mb-8 font-semibold text-gray-700 tracking-wide cursor-pointer mx-auto">
                    Welcome to WorldWideWohnung
                </p>
            </div>
            <form onSubmit={onSubmitHandler}>
                <div className="space-y-4">
                    <input type="file"
                        placeholder="Title"
                        className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-yellow-400"
                        onChange={(event) => {
                            onChangeForm("img_url", event);
                        }}
                    >
                    </input>
                    <input type="file"
                        placeholder="Photo of your house"
                        className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-yellow-400"
                        onChange={(event) => {
                            onChangeForm("img_url2", event);
                        }}
                    >
                    </input>    
                </div>
                <div className="text-center mt-6">
                    <button type="submit" className="py-3 w-64 text-x1 text-white bg-yellow-400 rounded-2x1 hover:pg-yellow-300 active:bg-yellow-500 outline-none"> Next</button>
                    
                </div>
            </form>
        </React.Fragment>
    )
}