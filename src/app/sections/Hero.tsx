"use client"
import React from 'react'
// import { Spotlight } from './ui/Spotlight'
import { TextGenerateEffect } from './ui/TextGenerate'
import MagicButton from './ui/MagicButton'

const Hero = () => {
  return ( 
    <div className='flex justify-center mt-36 my-20 z-10 '>
            <div className='max-w-[89vw] lg:max-w-[60vw] md:max-w-2xl  flex flex-col items-center justify-center'>
                <h1 className='uppercase tracking-widest text-xs text-center text-blue-100 max-w-96'>Get your things done with our College Finder chatbot</h1>

             <TextGenerateEffect className='text-center my-3 lg:text-3xl ' words='Chatbot to streamline admissions enquiries, providing instant assistance and reducing the workload on staff.' />

             <p className='text-center md:tracking-wider mb-4 text-sm md:text-lg lg:text-sm '>
             Empowering education through instant access, automation, and intelligent assistance
             </p>

             <a href="#">
                <MagicButton title="Ask Techtonix" />
             </a>
            </div>

    </div>
  )
}

export default Hero
