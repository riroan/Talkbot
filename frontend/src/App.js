import React, { useState } from 'react'
import url from './url'
import './App.css'

function App() {
	const [text, setText] = useState('')
	const [message, setMessage] = useState([])
	const onSubmit = () => {
		// setMessage([...message, [text, 'right']])
		fetch(url, {
			method: 'POST',
			headers: {
				Accept: 'application/json',
				'Content-Type': 'application/json',
			},
			body: JSON.stringify({ msg: text }),
		})
			.then(res => res.json())
			.then(res => {
				setMessage([...message, [text, 'right'], [res, 'left']])
				console.log(message)
			})
	}
	return (
		<div className="App">
			<div className="header">
				<input
					className="input"
					value={text}
					onChange={e => {
						setText(e.target.value)
					}}
					onKeyDown={e => {
						if (e.key === 'Enter') {
							onSubmit()
						}
					}}
				/>
				<button className="button" onClick={onSubmit}>
					보내기
				</button>
			</div>
			<div className="chat">
				{message.map((v, ix) => (
					<div key={ix} className={'msg ' + v[1]}>
						{v[0]}
					</div>
				))}
			</div>
		</div>
	)
}

export default App
