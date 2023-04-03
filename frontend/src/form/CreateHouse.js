import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import axios from "axios";
import { toast } from "react-toastify";




export default function House(props) {


    const navigate = useNavigate();
    //REgister Form 
    const [formHouse, setFormHouse] = useState({
        title: "",
        rent: "",
        no_rooms: "",
        size: "",
        additional_cost: "",
        total_rent: "",
        max_flatmates: "",
        exist_fmates: "",
        heating_type: "",
        heating_cost: "",
        city: "",
        zipcode: "",
        adress: "",
        description: "",
        min_duration: "",
        smoking_allowed: "",
        parking: "",
        postedby: "",
        img_url: "wwww",
        img_url2: "wwww",
        lat: "2.00",
        lng: "1.00",
        is_active:"True"

    });

    const onChangeForm = (label, event) => {
        switch (label) {
            case "title":
                setFormHouse({ ...formHouse, title: event.target.value });
                break;
            case "rent":
                setFormHouse({ ...formHouse, rent: event.target.value });
                break;
            case "no_rooms":
                setFormHouse({ ...formHouse, no_rooms: event.target.value });
                break;
            case "size":
                setFormHouse({ ...formHouse, size: event.target.value });
                break;
            case "additional_cost":
                setFormHouse({ ...formHouse, additional_cost: event.target.value });
                break;
            case "total_rent":
                setFormHouse({ ...formHouse, total_rent: event.target.value });
                break;
            case "max_flatmates":
                setFormHouse({ ...formHouse, max_flatmates: event.target.value });
                break;
            case "exist_fmates":
                setFormHouse({ ...formHouse, exist_fmates: event.target.value });
                break;
            case "heating_type":
                setFormHouse({ ...formHouse, heating_type: event.target.value });
                break;
            case "heating_cost":
                setFormHouse({ ...formHouse, heating_cost: event.target.value });
                break;
            case "city":
                setFormHouse({ ...formHouse, city: event.target.value });
                break;
            case "zipcode":
                setFormHouse({ ...formHouse, zipcode: event.target.value });
                break;
            case "adress":
                setFormHouse({ ...formHouse, adress: event.target.value });
                break;
            case "description":
                setFormHouse({ ...formHouse, description: event.target.value });
                break;
            case "min_duration":
                setFormHouse({ ...formHouse, min_duration: event.target.value });
                break;
            case "smoking_allowed":
                setFormHouse({ ...formHouse, smoking_allowed: event.target.value });
                break;
            case "parking":
                setFormHouse({ ...formHouse, parking: event.target.value });
                break;
            case "postedby":
                setFormHouse({ ...formHouse, postedby: event.target.value });
                break;
            case "img_url":
                setFormHouse({ ...formHouse, img_url: event.target.value });
                break;
            case "img_url2":
                setFormHouse({ ...formHouse, img_url2: event.target.value });
                break;
            case "lat":
                setFormHouse({ ...formHouse, lat: event.target.value });
                break;
            case "lng":
                setFormHouse({ ...formHouse, lng: event.target.value });
                break;
            /*case "is_active":
                setFormHouse({ ...formHouse, is_active: event.target.value });
                break;*/
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
                    <input type="text"
                        placeholder="Title"
                        className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-yellow-400"
                        onChange={(event) => {
                            onChangeForm("title", event);
                        }}
                    >
                    </input>
                    <input type="number"
                        placeholder="Cost of Renting"
                        className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-yellow-400"
                        onChange={(event) => {
                            onChangeForm("rent", event);
                        }}
                    >
                    </input>
                    <input
                        type="number"
                        placeholder="Total number of rooms"
                        className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-yellow-400"
                        onChange={(event) => {
                            onChangeForm("no_rooms", event);
                        }}
                    >
                    </input>
                    <input
                        type="number"
                        placeholder="Size of the place."
                        className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-yellow-400"
                        onChange={(event) => {
                            onChangeForm("size", event);
                        }}>
                    </input>
                    <input
                        type="number"
                        placeholder="Additional Cost"
                        className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-yellow-400"
                        onChange={(event) => {
                            onChangeForm("additional_cost", event);
                        }}
                    >
                    </input>
                    <input
                        type="number"
                        placeholder="Total rent?(Rent+Additional cost)"
                        className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-yellow-400"
                        onChange={(event) => {
                            onChangeForm("total_rent", event);
                        }}
                    >
                    </input>
                    <input
                        type="number"
                        placeholder="Number of the persons that can fit this aparment? "
                        className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-yellow-400"
                        onChange={(event) => {
                            onChangeForm("max_flatmates", event);
                        }}
                    >
                    </input>
                    <input
                        type="number"
                        placeholder="Number of persons that already live here? "
                        className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-yellow-400"
                        onChange={(event) => {
                            onChangeForm("exist_fmates", event);
                        }}
                    >
                    </input>
                    <input
                        type="text"
                        placeholder="Heating type?"
                        className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-yellow-400"
                        onChange={(event) => {
                            onChangeForm("heating_type", event);
                        }}
                    >
                    </input>
                    <input
                        type="text"
                        placeholder="Montly estimated heating cost?"
                        className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-yellow-400"
                        onChange={(event) => {
                            onChangeForm("heating_cost", event);
                        }}
                    >
                    </input>
                    <input
                        type="text"
                        placeholder="City"
                        className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-yellow-400"
                        onChange={(event) => {
                            onChangeForm("city", event);
                        }}
                    >
                    </input>
                    <input
                        type="number"
                        placeholder="Zipcode"
                        className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-yellow-400"
                        onChange={(event) => {
                            onChangeForm("zipcode", event);
                        }}
                    >
                    </input>
                    <input
                        type="text"
                        placeholder="Address"
                        className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-yellow-400"
                        onChange={(event) => {
                            onChangeForm("adress", event);
                        }}
                    >
                    </input>
                    <input
                        type="text"
                        placeholder="Description"
                        className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-yellow-400"
                        onChange={(event) => {
                            onChangeForm("description", event);
                        }}
                    >
                    </input>
                    <input
                        type="number"
                        placeholder="Minumum duration that tenant should stay here"
                        className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-yellow-400"
                        onChange={(event) => {
                            onChangeForm("min_duration", event);
                        }}
                    >
                    </input>
                    <input
                        type="text"
                        placeholder="Smoking allowed? Answer it True or False"
                        className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-yellow-400"
                        onChange={(event) => {
                            onChangeForm("smoking_allowed", event);
                        }}
                    >
                    </input>
                    <input
                        type="text"
                        placeholder="Is there a parking space of this property?"
                        className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-yellow-400"
                        onChange={(event) => {
                            onChangeForm("parking", event);
                        }}
                    >
                    </input>
                    <input
                        type="text"
                        placeholder="This property is posted by the owner or someone else?"
                        className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-yellow-400"
                        onChange={(event) => {
                            onChangeForm("postedby", event);
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