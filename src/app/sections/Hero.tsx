"use client";

import React, { useEffect, useRef } from "react";
import MagicButton from "./ui/MagicButton";
import { TextGenerateEffect } from "./ui/TextGenerate";

const useGridEffect = () => {
  const gridRef = useRef<HTMLDivElement>(null);

  useEffect(() => {
    const grid = gridRef.current;
    if (!grid) return;

    const createBlocks = () => {
      const screenWidth = window.innerWidth;
      const screenHeight = window.innerHeight;
      const blockSize = 50; // matches your CSS
      const numCols = Math.ceil(screenWidth / blockSize);
      const numRows = Math.ceil(screenHeight / blockSize);

      grid.style.gridTemplateColumns = `repeat(${numCols}, 1fr)`;
      grid.style.gridTemplateRows = `repeat(${numRows}, 1fr)`;

      for (let i = 0; i < numCols * numRows; i++) {
        const block = document.createElement("div");
        block.addEventListener("mouseover", () => highlightBlock(block));
        grid.appendChild(block);
      }
    };

    const highlightBlock = (block: HTMLDivElement) => {
      block.classList.add("highlight");
      setTimeout(() => block.classList.remove("highlight"), 300);

      // Highlight a random neighbor
      const neighbors = [
        block.previousElementSibling,
        block.nextElementSibling,
        grid.children[Array.from(grid.children).indexOf(block) - Math.floor(grid.children.length / Math.sqrt(grid.children.length))],
        grid.children[Array.from(grid.children).indexOf(block) + Math.floor(grid.children.length / Math.sqrt(grid.children.length))]
      ].filter(Boolean);

      const randomNeighbor = neighbors[Math.floor(Math.random() * neighbors.length)] as HTMLDivElement;
      if (randomNeighbor) {
        randomNeighbor.classList.add("highlight");
        setTimeout(() => randomNeighbor.classList.remove("highlight"), 300);
      }
    };

    createBlocks();

    return () => {
      grid.innerHTML = '';
    };
  }, []);

  return gridRef;
};

const Hero: React.FC = () => {
  const gridRef = useGridEffect();

  return (
    <div className="relative flex justify-center items-center h-screen overflow-hidden">
      <div ref={gridRef} className="grid-background absolute top-0 left-0 w-full h-full"></div>
      
      <div className="max-w-[89vw] lg:max-w-[60vw] md:max-w-2xl flex flex-col items-center justify-center z-10">
        <h1 className="uppercase tracking-widest text-xs text-center text-blue-100 max-w-96">
          Get your things done with our College Finder chatbot
        </h1>
        <TextGenerateEffect
          className="text-center my-3 lg:text-3xl"
          words="Chatbot to streamline admissions enquiries, providing instant assistance and reducing the workload on staff."
        />
        <p className="text-center md:tracking-wider mb-4 text-sm md:text-lg lg:text-sm">
          Education made easy, <b>COLLEGE SAHAYAK</b> ke saath!!
        </p>
        <a href="#">
          <MagicButton title="Ask Sahayak" />
        </a>
      </div>
    </div>
  );
};

export default Hero;