import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
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
  


export default function Register(props) {
      /*const options = [
            { value: "", label: "Select Your Gender !" },
            { value: "MALE", label: "Male" },
            { value: "FEMALE", label: "Female" },
      ];*/

      const navigate = useNavigate();
      //REgister Form 
      const [formRegister, setFormRegister] = useState({
            username: "",
            password: "",
            email: "",
            max_rent: "",
            smoking: "",
            religion: "",
            profession: "",
            want_fmates: "",
            hobbies: "",
            languages: "",
            role: ""
      });

      const onChangeForm = (label, event) => {
            switch (label) {
                  case "username":
                        setFormRegister({ ...formRegister, username: event.target.value });
                        break;
                  case "password":
                        setFormRegister({ ...formRegister, password: event.target.value });
                        break;
                  case "email":
                        setFormRegister({ ...formRegister, email: event.target.value });
                        break;
                  case "max_rent":
                        setFormRegister({ ...formRegister, max_rent: event.target.value });
                        break;
                  case "smoking":
                        setFormRegister({ ...formRegister, smoking: event.target.value });
                        break;
                  case "religion":
                        setFormRegister({ ...formRegister, religion: event.target.value });
                        break;
                  case "profession":
                        setFormRegister({ ...formRegister, profession: event.target.value });
                        break;
                  case "want_fmates":
                        setFormRegister({ ...formRegister, want_fmates: event.target.value });
                        break;
                  case "hobbies":
                        setFormRegister({ ...formRegister, hobbies: event.target.value });
                        break;
                  case "languages":
                        setFormRegister({ ...formRegister, languages: event.target.value });
                        break;
                  case "role":
                        setFormRegister({ ...formRegister, role: event.target.value });
                        break;
            }


      }

      const onSubmitHandler = async (event) => {
            event.preventDefault()
            console.log(formRegister)

            await axios.post("http://127.0.0.1:8000/users/", formRegister)
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
            <React.Fragment> <Navbar/>
                  <div className="min-h-screen  bg-yellow-500  flex justify-center items-center">
                        <div className="py-12 px-12 bg-white rounded-2xl shadow-xl z-20">
                        <div>
                              <h1 className="text-3x1 font-bold text-center mb-4 cursor-pointer">
                                    Create Your Account
                              </h1>
                              <p className="w-80 text-center text-sm mb-8 font-semibold text-gray-700 tracking-wide cursor-pointer mx-auto">
                                    Welcome to WorldWideWohnung
                              </p>
                        </div>
                        <form onSubmit={onSubmitHandler}>
                              <div className="space-y-4">
                                    <input type="text"
                                          placeholder="Username"
                                          className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-yellow-400"
                                          onChange={(event) => {
                                                onChangeForm("username", event);
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
                                    <input
                                          type="email"
                                          placeholder="Email"
                                          className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-yellow-400"
                                          onChange={(event) => {
                                                onChangeForm("email", event);
                                          }}
                                    >
                                    </input>
                                    <input
                                          type="number"
                                          placeholder="Maximum Rent"
                                          className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-yellow-400"
                                          onChange={(event) => {
                                                onChangeForm("max_rent", event);
                                          }}>
                                    </input>
                                    <input
                                          type="text"
                                          placeholder="Do you smoke?"
                                          className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-yellow-400"
                                          onChange={(event) => {
                                                onChangeForm("smoking", event);
                                          }}
                                    >
                                    </input>
                                    <input
                                          type="text"
                                          placeholder="Religion?"
                                          className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-yellow-400"
                                          onChange={(event) => {
                                                onChangeForm("religion", event);
                                          }}
                                    >
                                    </input>
                                    <input
                                          type="text"
                                          placeholder="What is your profession?"
                                          className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-yellow-400"
                                          onChange={(event) => {
                                                onChangeForm("profession", event);
                                          }}
                                    >
                                    </input>
                                    <input
                                          type="text"
                                          placeholder="Are you looking for a Flatmate/s?"
                                          className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-yellow-400"
                                          onChange={(event) => {
                                                onChangeForm("want_fmates", event);
                                          }}
                                    >
                                    </input>
                                    <input
                                          type="text"
                                          placeholder="What is your Hobbies?"
                                          className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-yellow-400"
                                          onChange={(event) => {
                                                onChangeForm("hobbies", event);
                                          }}
                                    >
                                    </input>
                                    <input
                                          type="text"
                                          placeholder="Which languages do you speak?"
                                          className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-yellow-400"
                                          onChange={(event) => {
                                                onChangeForm("languages", event);
                                          }}
                                    >
                                    </input>
                                    <input
                                          type="text"
                                          placeholder="What is your role? If you are a landlord type landlord o.w you can type Tenant"
                                          className="block text-sm py-3 px-4 rounded-lg w-full border outline-none focus:ring focus:outline-none focus:ring-yellow-400"
                                          onChange={(event) => {
                                                onChangeForm("role", event);
                                          }}
                                    >
                                    </input>
                              </div>
                              <div className="text-center mt-6">
                                    <button type="submit" className="py-3 w-64 text-x1 text-white bg-yellow-400 rounded-2x1 hover:pg-yellow-300 active:bg-yellow-500 outline-none"> Create Account</button>
                                    <p className="mt-4 text-sm">Already have an Account?{" "}
                                          <Link to="/?signin"
                                                onClick={() => {
                                                      props.setPage("login")

                                                }}
                                          >
                                                <span className="underline cursor-pointer"> Sign In</span>
                                          </Link>

                                    </p>

                              </div>
                        </form>
                  </div>
            </div>

            </React.Fragment >
      )
}