import React from 'react'

const Loader = () => {
  return (
    <div><svg
    xmlns="http://www.w3.org/2000/svg"
    viewBox="0 0 100 100"
    preserveAspectRatio="xMidYMid"
    width="15px"
    height="15px"
    style={{ shapeRendering: 'auto', display: 'block', background: 'transparent' }}
    xmlnsXlink="http://www.w3.org/1999/xlink"
  >
    <g>
      <circle
        strokeDasharray="164.93361431346415 56.97787143782138"
        r="35"
        strokeWidth="10"
        stroke="#546a7b"
        fill="none"
        cy="50"
        cx="50"
      >
        <animateTransform
          attributeName="transform"
          type="rotate"
          dur="1s"
          repeatCount="indefinite"
          keyTimes="0;1"
          values="0 50 50;360 50 50"
        />
      </circle>
      <g></g>
    </g>
  </svg></div>
  )
}

export default Loader