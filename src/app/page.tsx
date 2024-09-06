// import Image from "next/image";
// import Features from "./sections/Features";
import Features from "./sections/Features";
import Footer from "./sections/Footer";
import { Header } from "./sections/Header";
import Hero from "./sections/Hero";

export default function Home() {
  return (
   <div>
      <Header/>
      <Hero/>
      {/* <Features/> */}
      <Features/>
      <Footer/>
   </div>
  );
}
