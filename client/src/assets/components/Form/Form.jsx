import React from "react"
import Loader from "../LoaderIcon"

const Form = ({ handleChange, handleInput, handleFileInput, handleFileClose, handleSubmit, file, query, loading,fintec }) => {

return (
    <>
    <form id='form' className='w-full bg-[#122C3F] max-h-100 border-[0.8px] border-[#546A7B] rounded-[1.3rem] p-3 text-white align-top' onSubmit={handleSubmit}>
        <div className='grid'>
            {file&&<div className='border-1 border-[#546A7B] w-25 h-25 p-4 overflow-hidden text-wrap rounded-2xl text-[#546A7B] bg-[rgba(174,235,152,0.2)] relative group'>
                {file.name}
                <svg xmlns="http://www.w3.org/2000/svg" height="1rem" viewBox="0 -960 960 960" width="1rem" fill="#e8eaed" className='absolute right-2 top-2 hidden group-hover:block cursor-pointer' onClick={handleFileClose}><path d="m256-200-56-56 224-224-224-224 56-56 224 224 224-224 56 56-224 224 224 224-56 56-224-224-224 224Z" /></svg>
            </div>}
            <textarea className='resize-none overflow-hidden h-fit !overscroll-y-none focus:outline-none text-[0.9rem]' onInput={handleInput} value={query} onChange={handleChange}/>
            <div className='uploads flex content-center gap-3'>
                <div className='flex grow gap-2'>
                    <input id="upload" className="p-2 border-1 border-[#546A7B] rounded-xl hidden peer/submit" type='file' onInput={handleFileInput}/>
                    <label htmlFor="upload" className="p-2 border-1 border-[#546A7B] rounded-xl peer-hover/submit:bg-[rgba(84,106,123,0.5)] cursor-pointer"><svg xmlns="http://www.w3.org/2000/svg" height="15px" viewBox="0 -960 960 960" width="15px" fill="#546A7B"><path d="M720-330q0 104-73 177T470-80q-104 0-177-73t-73-177v-370q0-75 52.5-127.5T400-880q75 0 127.5 52.5T580-700v350q0 46-32 78t-78 32q-46 0-78-32t-32-78v-370h80v370q0 13 8.5 21.5T470-320q13 0 21.5-8.5T500-350v-350q-1-42-29.5-71T400-800q-42 0-71 29t-29 71v370q-1 71 49 120.5T470-160q70 0 119-49.5T640-330v-390h80v390Z"/></svg></label>
                    {fintec?<div className="finance p-1 px-3 content-center border-1 rounded-3xl text-[#A1E887] text-[.75rem] hover:bg-[rgba(84,106,123,0.5)] leading-1 h-[100%] cursor-pointer">fintech</div>:<div className="finance p-1 px-3 content-center border-1 rounded-3xl text-[#546A7B] text-[.75rem] hover:bg-[rgba(84,106,123,0.5)] leading-1 h-[100%] cursor-pointer">fintech</div>}
                </div>
                <button className={`p-2 bg-[#A1E887] ${loading?'opacity-50 cursor-not-allowed':'cursor-pointer'} rounded-xl cursor-pointer`} type='submit' disabled={loading}>
                {loading?<Loader/>:<svg xmlns="http://www.w3.org/2000/svg" height="15px" viewBox="0 -960 960 960" width="15px" fill="#546A7B" ><path d="M440-160v-487L216-423l-56-57 320-320 320 320-56 57-224-224v487h-80Z"/></svg>}
                </button>
            </div>
        </div>
    </form>
    </>
)
}

export default Form