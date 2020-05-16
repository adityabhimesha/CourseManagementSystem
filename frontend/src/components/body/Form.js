import React, { Component,Fragment } from 'react'
import axios from 'axios';

export class Content extends Component {

    constructor(props) 
    { 
        super(props); 
        this.state = { 
            styles:{
                marginTop : "0px",
                marginBottom : "0px",
                position: "relative",

            },
            formValues: {},
            success:{
                display:"none"
            }
    }; 
    }
    
    handleChange(event) {
        event.preventDefault();
        let formValues = this.state.formValues;
        formValues[event.target.name] = event.target.value;

        this.setState({formValues})
    }

    handleSubmit(event) {
        event.preventDefault();
        let config = {
            headers: {
              'Content-Type': 'application/json; charset=UTF-8',
            }
          }
        axios.post('http://127.0.0.1:8000/api/contact/',this.state.formValues, config).then(res =>{
                    console.log(res.data);
                    this.setState({
                        success:{
                            display:"block"
                        }
                    })
            })
      }


    componentDidMount(props) {
    this.setState({
        styles: {
        marginTop:"10%",
        marginBottom: "0px",
        position: "relative",
        color:"black",
        }
    })

        
      }

    render() {

        return (
            <div>
                <div ref="child" className="bg-dark" style={this.state.styles}>
                  <div className="container text-primary pt-4 pb-4">
                      <h1>What's your thoughts on us?</h1>
                      <h4 className="text-light" style={this.state.subtitle}>Welcome To The React Version Of The Contact Page.</h4>
                  </div>
                </div>

                <div className="container mt-5 mb-5">
                <form onSubmit={this.handleSubmit.bind(this)} className="row text-dark" style={{fontWeight:"bold"}}>
                    <label className="col-md-12">
                        First Name:<br/>
                        <input className="w-100 pt-2" type="text" name="fname" value={this.state.formValues["fname"]} onChange={this.handleChange.bind(this)}/>
                    </label>
                    <label className="col-md-12">
                        Last Name:<br/>
                        <input className="w-100 pt-2" type="text" name="lname" value={this.state.formValues["lname"]} onChange={this.handleChange.bind(this)} />
                    </label>
                    <label className="col-md-12">
                        Email:<br/>
                        <input className="w-100 pt-2" className="w-100" type="email" name="email" value={this.state.formValues["email"]} onChange={this.handleChange.bind(this)} />
                    </label>
                    <label className="col-md-12">
                        Phone Number:<br/>
                        <input className="w-100 pt-2" className="w-100" type="number" name="phone" value={this.state.formValues["number"]} onChange={this.handleChange.bind(this)} />
                    </label>
                    <label className="col-md-12">
                        What's on your mind?:<br/>
                        <textarea className="w-100 pt-2" type="a" name="body" value={this.state.formValues["body"]} onChange={this.handleChange.bind(this)} />
                    </label>
                    <label className="col-md-12">
                        <input type="submit" value="Submit" className="mt-5 btn btn-primary w-25"/>
                    </label>
                    
                </form>
                <div id="success" className="mt-5 mb-3 alert alert-success text-center" style={this.state.success}>
                    <p>Your Response has Successfully been recorded!!
                        Thank You.
                    </p>
                </div>
                </div>
            </div>

            
        )
    }
}

export default Content
