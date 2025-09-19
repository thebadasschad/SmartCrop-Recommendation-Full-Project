import React, {useState} from 'react';

export default function App(){
  const [form, setForm] = useState({pH:6.5,N:300,P:40,K:200,avg_temp:25,rainfall:800,humidity:60,altitude:300,soil_type:'loam'})
  const [resp, setResp] = useState(null)

  const handleChange = (e) => {
    const {name, value} = e.target
    setForm({...form,[name]: value})
  }

  const submit = async () => {
    const res = await fetch('http://localhost:8000/predict', {
      method:'POST', headers:{'Content-Type':'application/json'}, body: JSON.stringify(form)
    })
    const data = await res.json()
    setResp(JSON.stringify(data))
  }

  return (
    <div style={{padding:20,fontFamily:'sans-serif'}}>
      <h2>SmartCrop — Demo</h2>
      <div style={{display:'grid',gridTemplateColumns:'1fr 1fr',gap:8,maxWidth:600}}>
        {Object.keys(form).map(k => (
          <label key={k} style={{display:'block'}}>
            {k}
            <input name={k} value={form[k]} onChange={handleChange} style={{width:'100%'}} />
          </label>
        ))}
      </div>
      <button onClick={submit} style={{marginTop:12}}>Predict</button>
      <pre style={{marginTop:12}}>{resp}</pre>
    </div>
  )
}
