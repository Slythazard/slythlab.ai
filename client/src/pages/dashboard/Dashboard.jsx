import React from 'react'
import { useParams } from 'react-router-dom'

const Dashboard = () => {
    const {id} = useParams()
  return (
    <div><h1 className='text-white text-4xl'>{id}</h1></div>
  )
}

export default Dashboard