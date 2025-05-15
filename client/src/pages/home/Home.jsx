import "../../assets/styles/Home.css"
import Form from '../../assets/components/Form/Form'
import Navbar from "../../assets/components/Navigation"
import React,{ useState} from 'react'
import axios from "axios"
import ReactMarkdown from 'react-markdown'
// import axios from 'axios'
const API_URL = import.meta.env.VITE_API_URL

const Home = () => {

  const [answer,setAnswer]=useState()
  const [query,setQuery]=useState()
  const [file, setFile]=useState(null)
  const [loading, setLoading]=useState(false)
  const [fintec, setFintec] = useState(false)
  const typeOfTime = 'Morning'
  const user = 'User'

const handleInput = (e) => {
    e.target.style.height = 'auto';
    const maxHeight = 300;
    const scrollHeight = e.target.scrollHeight;
    
    e.target.style.overflowY = scrollHeight > maxHeight ? 'auto' : 'hidden';
    e.target.style.height = `${Math.min(scrollHeight, maxHeight)}px`;}

    const handleChange=(e)=>{
        setQuery(e.target.value)
    }

const handleSubmit = async (e)=>{
    e.preventDefault()
    setLoading(true)
    const formData = new FormData()

    if(query || file || query && file){
        formData.append('query',query)
        formData.append('file',file)
    }

    await axios.post(`${API_URL}/upload`,formData,{headers:{
        'Content-Type':'multipart/form-data'
    }}).then(response=>{
      setAnswer(response)
    })

    setLoading(false)
    setFile(null)
    setFintec(false)
    // setQuery('')
}

const handleFileInput=(e)=>{
  const filesX = e.target.files
  const arr = ['xlsx','xlx','csv']
  const filename = (filesX[0].name)
  const extension = filename.split('.').pop()
  const isFinance = arr.includes(`${extension}`)
  console.log(filename)
  console.log(extension)
  console.log(isFinance)
  if (filesX){
    setFile(filesX[0])
    if(isFinance){
      setFintec(true)
    }
  }
}
  

  const handleFileClose=()=>{
      file!=null&&setFile(null)
  }

  return (
    <div className="w-[90%] mx-auto h-[100%]">
    <Navbar/>
    <div className='w-[60%] mx-auto h-[100%]'>
      {answer?(
      <div className="text-xl text-gray-700 h-[100%] mt-5">
        <div className="mt-0">
          <div className="border-1 p-4 rounded-2xl text-[1rem] text-white">{query}?</div>
          <div className="py-6 px-2 text-[1rem] text-white"><ReactMarkdown>{answer.data?.answer.replace(/\\n/g, '\n') ?? "No answer available"}</ReactMarkdown></div>
        </div>
      <div className="sticky bottom-0"><Form/></div>
    </div>):
    (<div className="mt-50 w-[90%] mx-auto flex flex-col">
      <h1 className='text-[#546A7B] text-5xl p-5 self-center'>Good {typeOfTime} {user}</h1>
      <Form
      handleChange={handleChange}
      handleInput={handleInput}
      handleFileInput={handleFileInput}
      handleFileClose={handleFileClose}
      handleSubmit={handleSubmit}
      file={file}
      query={query}
      loading={loading}
      fintec={fintec}></Form>
    </div>)}
    </div>
    </div>
  )
}
export default Home