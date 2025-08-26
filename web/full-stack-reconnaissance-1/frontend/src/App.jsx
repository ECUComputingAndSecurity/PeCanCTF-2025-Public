import { useState } from "react";
import reactLogo from "./assets/react.svg";
import viteLogo from "/kaled.aljebur.ico";
import "./App.css";
import "bootstrap/dist/css/bootstrap.min.css";
import { BrowserRouter, Routes, Route, Link } from "react-router-dom";
import Home from "./components/HomePage";
import Test from "./components/Test";
import Help from "./components/Help";
import Network from "./components/Network";
import Web from "./components/Web";
import Mobile from "./components/Mobile";
import Iot from "./components/Iot";
import Cloud from "./components/Cloud";
import Social from "./components/Social";
import Physical from "./components/Physical";
import Client from "./components/Client";
import Information from "./components/Information";
import NotFound from "./components/NotFound";

function App() {
  return (
    <div className="container">
      <h1 className="mt-5 mb-5 text-center">
        <b>
          <span className="text-primary">Cyber MiniBlog!</span>
        </b>
      </h1>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/test" element={<Test />} />
          <Route path="/help" element={<Help />} />
          <Route path="/networking" element={<Network />} />
          <Route path="/websites" element={<Web />} />
          <Route path="/mobilestuff" element={<Mobile />} />
          <Route path="/clouding" element={<Cloud />} />
          <Route path="/socialspace" element={<Social />} />
          <Route path="/clientendpoint" element={<Client />} />
          <Route path="/physicalenviroments" element={<Physical />} />
          <Route path="/iotdevices" element={<Iot />} />
          <Route path="/info" element={<Information />} />
          <Route path="*" element={<NotFound />} />
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
