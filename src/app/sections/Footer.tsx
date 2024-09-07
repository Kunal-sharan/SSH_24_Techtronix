import React from 'react'
import { FaExternalLinkAlt } from "react-icons/fa";
import Logo from '../assets/logo.svg'

const Footer = () => {
  return (
    <footer className=' bg-gradient-to-b  from-[#2e2200] to-black pt-32 h-[400px]'>
              <div className="container mx-auto  max-w-6xl px-4">
                <div className="flex justify-evenly items-center ">
                    {/* Logo and About */}
                    <div className="flex flex-col items-center  md:items-start">
                        <Logo className="h-12 w-12 mb-4" />
                        <p className="text-center md:text-left w-[300px] text-white/70">
                            Our platform helps students find the best colleges and make informed decisions for their academic future.
                        </p>
                    </div>
                    
                    {/* Navigation */}
                    <div className="flex flex-col items-center md:items-start">
                        <h4 className="text-lg font-semibold mb-4">Quick Links</h4>
                        <nav className="flex flex-col gap-2 text-sm">
                            <a href="#" className="text-white/70 flex justify-center items-center gap-2 hover:text-white transition"> <p> Top-10 Universities of Rajasthan </p>  <FaExternalLinkAlt /></a>
                            <a href="#" className="text-white/70 hover:text-white transition">Btech-CSE best colleges</a>
                            <a href="#" className="text-white/70 hover:text-white transition">High paying jobs in India</a>
                            <a href="#" className="text-white/70 hover:text-white transition">Best Career options to choose</a>
                        </nav>
                    </div>

                    {/* Social Media */}
                    <div className="flex flex-col items-center md:items-start">
                        <h4 className="text-lg font-semibold mb-4">Follow Us</h4>
                        <div className="flex gap-4">
                            <a href="#" className="text-white/70 hover:text-white transition">
                                <svg className="h-6 w-6" fill="currentColor" viewBox="0 0 24 24">
                                    {/* Icon for Facebook */}
                                    <path d="M9 8H6v4h3v12h5V12h3.642l.358-4H14V6.355C14 5.646 14.234 5 15 5h2V0h-4C10.624 0 9 1.646 9 4.309V8z"/>
                                </svg>
                            </a>
                            <a href="#" className="text-white/70 hover:text-white transition">
                                <svg className="h-6 w-6" fill="currentColor" viewBox="0 0 24 24">
                                    {/* Icon for Twitter */}
                                    <path d="M24 4.557a9.939 9.939 0 0 1-2.828.775 4.939 4.939 0 0 0 2.165-2.725 9.846 9.846 0 0 1-3.127 1.195 4.925 4.925 0 0 0-8.392 4.485A13.98 13.98 0 0 1 1.671 3.149a4.917 4.917 0 0 0 1.523 6.569 4.907 4.907 0 0 1-2.231-.616v.061a4.927 4.927 0 0 0 3.946 4.827 4.937 4.937 0 0 1-2.224.084 4.926 4.926 0 0 0 4.6 3.417 9.875 9.875 0 0 1-6.12 2.108c-.398 0-.79-.023-1.177-.068A13.92 13.92 0 0 0 7.548 22c9.142 0 14.307-7.721 14.307-14.426 0-.22-.005-.438-.015-.656A10.254 10.254 0 0 0 24 4.557z"/>
                                </svg>
                            </a>
                            <a href="#" className="text-white/70 hover:text-white transition">
                                <svg className="h-6 w-6" fill="currentColor" viewBox="0 0 24 24">
                                    {/* Icon for LinkedIn */}
                                    <path d="M19 0h-5a5 5 0 0 0-5 5v14a5 5 0 0 0 5 5h5a5 5 0 0 0 5-5V5a5 5 0 0 0-5-5zm-2.5 16h-2v-4h2v4zm1-10a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3zM5 16H3v-8h2v8zm-1-9a1.5 1.5 0 1 1 0-3 1.5 1.5 0 0 1 0 3z"/>
                                </svg>
                            </a>
                        </div>
                    </div>
                </div>

                {/* Bottom Line */}
                <div className="border-t border-white/15 mt-8 pt-4 text-center text-sm text-white/70">
                    <p>&copy; 2024 College Finder. All rights reserved.</p>
                </div>
            </div>
    </footer>
  )
}

export default Footer
