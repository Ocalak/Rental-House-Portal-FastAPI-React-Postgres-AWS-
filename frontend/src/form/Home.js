import React, { useState } from "react";
import { Link, useNavigate } from "react-router-dom";
import axios from "axios";
import { toast } from "react-toastify";


export default function Home() {
    return (
        <React.Fragment>
                    <figure>
                        <img src="/Users/ocalkaptan/Desktop/tenant.png" alt="Tenant">
                            <figcaption>Search For Flats</figcaption>
                        </img>
                    </figure>
                
                
                    <figure>

                        <img src="/Users/ocalkaptan/Desktop/land.png" alt="Landlord">
                            <figcaption>List Your Property</figcaption>
                        </img>

                    </figure>
                



        </React.Fragment>
    )






}