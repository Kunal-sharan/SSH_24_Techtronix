"use client"
import React from 'react'
import project1 from '../assets/icons1.jpg'
import project2 from '../assets/icons2.jpg'
import { motion } from 'framer-motion'
import Image from 'next/image'
import project3 from '../assets/icon3.jpg'
import project4 from '../assets/icons4.jpg'
import project5 from '../assets/icon5.jpg'
import project6 from '../assets/icon6.jpg'
import project7 from '../assets/icon7.jpg'
import project8 from '../assets/icon8.jpg'

const projects = [{
    title: "AI-Powered Admission Assistant",
    desc: "An intelligent chatbot that provides 24/7 assistance for admission-related queries, including eligibility criteria, application processes, and deadlines for engineering and polytechnic institutes in Rajasthan.",
    location: "Department of Technical Education, Rajasthan",
    link: "#",
    src: project3
  },
  {
    title: "College Information Hub",
    desc: "A comprehensive database-driven chatbot that offers detailed information about various engineering and polytechnic colleges under the Department of Technical Education, including courses offered, faculty details, and infrastructure.",
    location: "Centralized Platform for Rajasthan Technical Education",
    link: "#",
    src: project4
  },
  {
    title: "Scholarship and Financial Aid Guide",
    desc: "An AI assistant that provides up-to-date information on available scholarships, fee structures, and financial aid options for students seeking admission to technical institutes in Rajasthan.",
    location: "Accessible across Rajasthan",
    link: "#",
    src: project5
  },
  {
    title: "Career Counseling and Placement Bot",
    desc: "An intelligent system that offers insights into career prospects, placement opportunities, and alumni success stories for different branches of engineering and polytechnic programs in Rajasthan.",
    location: "Virtual Career Center for Rajasthan Technical Education",
    link: "#",
    src: project6
  },
  {
    title: "Multilingual Technical Education Assistant",
    desc: "A chatbot with Natural Language Processing capabilities, providing information in English, Hindi, and other regional languages to ensure wide accessibility for all stakeholders in Rajasthan's technical education system.",
    location: "Language-Inclusive Platform for Rajasthan",
    link: "#",
    src: project7
  },
  {
    title: "Analytics Dashboard for Education Insights",
    desc: "A data-driven tool that analyzes user interactions with the chatbot to provide valuable insights to the Department of Technical Education, helping optimize services and address common concerns efficiently.",
    location: "Department of Technical Education, Rajasthan",
    link: "#",
    src: project8
  }
]

const Features = () => {
  return (
    <div className='text-white bg-gradient-to-b items-center  from-black  to-[#2e2200]  py-18 mt-40  ' id='portfolio'>
                    <motion.div  initial={{opacity:0,y:75}}
                              whileInView={{opacity:1,y:0}}
                              viewport={{once:true}}
                              transition={{duration:0.5,delay:0.25}}
                              className='text-6xl flex gap-4 mx-auto p-4 my-12 tracking-wider mt-20 ml-28  font-semibold text-purple-200'>
                              <p> How it </p>  <p className='text-red-500'> works? </p>  
                    </motion.div>
                
                    <div className='max-w-[1000px] mx-auto mt-20 space-y-24'>
                        {projects.map((project,index) => (
                            <motion.div
                              key={index}
                              initial={{opacity:0,y:75}}
                              whileInView={{opacity:1,y:0}}
                              viewport={{once:true}}
                              transition={{duration:0.5,delay:0.25}}
                              className={`mt-12 flex ${index%2==1 ? " flex-col-reverse md:flex-row-reverse  gap-12" : "flex-col md:flex-row"}`}
                             >
                                    
                                    <div className='space-y-2  max-w-[600px]'>
                                        <h2 className='text-7xl my-4 text-white/70'>{`0${index+1}`}</h2>
                                        <h2 className='text-4xl'>{project.title}</h2>
                                        <p className='text-lg text-white/70 break-words pt-4 pb-4 pr-4'>{project.desc}</p>
                                        <p className='text-xl text-orange-500 font-semibold'> {project.location}</p>
                                        <div className='w-64 h-[1px] bg-gray-400 my-4'>
                                            <a href="#" className='mr-6'>Link</a>
                                        </div>
                                    </div>

                                    <div className='justify-center  flex items-center'>
                                        <Image src={project.src} alt={project.title} className='h-[350px] border  rounded-xl w-[500px] object-cover ' />
                                    </div>
                            </motion.div>
                        ))}
                    </div>
    </div>
  )
}

export default Features
