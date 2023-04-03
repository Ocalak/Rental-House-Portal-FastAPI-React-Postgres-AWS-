import React, { useState } from "react";
import { Link } from "react-router-dom";
import axios from "axios";
import { toast } from "react-toastify";


function Navbar() {
    return (
      <nav className="flex justify-between items-center h-16 bg-yellow text-white">
      
       <div className="pl-1 flex items-center">
        
    
        
      </div>
        <div className="pl-8">
        
        </div>
        <div className="pr-8">
          <ul className="flex">
          <li className="mr-6">
              <Link to="/faq"className="text-black">Home</Link>
            </li>
        
            <li className="mr-6">
              <Link to="/?register" className="text-black"
              >About</Link>
            </li>
            
            <li>
              <Link to="/login"className="text-black">Contact</Link>
            </li>
          </ul>
        </div>
      </nav>
    );
  }

export default function Login(props) {
    const [loginForm, setLoginform] = useState({
        email: "",
        password: "",
    });

    const onChangeForm = (label, event) => {
        switch (label) {
            case "email":
                setLoginform({ ...loginForm, email: event.target.value });
                break;
            case "password":
                setLoginform({ ...loginForm, password: event.target.value });
                break;
        }
    };

    const onSubmitHandler = async (event) => {
        event.preveventDefault();
        console.log(loginForm);
        await axios.post("http://localhost:8000/login/token", loginForm)
            .then((response) => {
                console.log(response);
                localStorage.setItem("auth_token", response.data.result.access_token);
                localStorage.setItem("auth_token_type", response.data.result.token_type);

                toast.success(response.data.detail);

                setTimeout(() => {
                    window.location.reload();
                }, 1000);
            })
            .catch((error) => {
                console.log(error);
                toast.error(error.response.data.detail);
            });
    }


    return (
        <React.Fragment> <Navbar/>
        <div className="min-h-screen  bg-yellow-500  flex justify-center items-center">
            <div className="py-12 px-12 bg-white rounded-2xl shadow-xl z-20">
                <div>
                    <h1 className="text-3x1 font-bold text-center mb-4 cursor-pointer">
                        Welcome to WorldWideWohnung
                    </h1>
                    <p className="w-80 text-center text-sm mb-8 font-semibold text-gray-700 tracking-wide cursor-pointer mx-auto">
                        Please login to your account
                    </p>
                </div>
                <form onSubmit={onSubmitHandler}>
                    <div className="space-y-4">
                        <input type="text"
                            placeholder="Email"
                            className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-yellow-400"
                            onChange={(event) => {
                                onChangeForm("email", event)
                            }}
                        >
                        </input>
                        <input type="password"
                            placeholder="Password"
                            className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-yellow-400"
                            onChange={(event) => {
                                onChangeForm("password", event);
                            }}
                        >
                        </input>

                    </div>
                    <div className="text-center mt-6">
                        <button type="submit" className="py-3 w-64 text-x1 text-white bg-yellow-400 rounded-2x1 hover:pg-yellow-300 active:bg-yellow-500 outline-none"> Sign In</button>
                        <p className="mt-4 text-sm">You don't have an Account?{" "}
                            <Link to="/?register"
                                onClick={() => {
                                    props.setPage("register")

                                }}
                            >
                                <span className="underline cursor-pointer"> Register</span>
                            </Link>
                            
                        </p>

                    </div>
                </form>
            </div>
        </div>
        </React.Fragment>
    )
}