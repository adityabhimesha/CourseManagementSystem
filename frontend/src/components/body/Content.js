import React, { Component,Fragment } from 'react'
import About_card from './About_card';
import TeachersContainer from './Teachers';
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
            subtitle:{
              color:"grey",
            },
            teachers:{
              data:"",
            }
    }; 
    } 
      componentDidMount(props) {
        this.setState({
          styles: {
            marginTop:"10%",
            marginBottom: "0px",
            position: "relative",
            color:"black",
          },
          subtitle:{
            color:"white",
          } 
        })

        axios.get('http://127.0.0.1:8000/api/teachers',{
          crossdomain: true
        }).then(res =>{
                this.setState({
                    teachers:{
                      data : res.data,
                    }
                });
                console.log("success");
            })
      }

    render() {
        const card_data =[
          {
            image:"/static/images/hero_1.jpg",
            heading:"Why Academics Works?",
            textarea:"Lorem ipsum dolor sit amet consectetur adipisicing elit. At itaque dolore libero corrupti! Itaque, delectus?"
          },
          {
            image:"/static/images/hero_2.jpg",
            heading:"Personalized Learning",
            textarea:"Modi sit dolor repellat esse! Sed necessitatibus itaque libero odit placeat nesciunt, voluptatum totam facere.Modi sit dolor repellat esse!At itaque dolore libero corrupti! Itaque, delectus?"
          },
          {
            image:"/static/images/blog_3.jpg",
            heading:"Our Philosphy",
            textarea:"Lorem ipsum dolor, sit amet consectetur adipisicing elit. Tempora facere consectetur at fuga veritatis quidem natus minima itaque ducimus totam maiores ad, ipsum facilis laudantium officia expedita beatae magnam cumque obcaecati culpa aut sit nostrum vero quaerat. Fugiat, hic!"
          },

        ]

        return (
          <div>
                <div ref="child" className="bg-dark" style={this.state.styles}>
                  <div className="container text-primary pt-4 pb-4">
                      <h1>Hello!!</h1>
                      <h4 style={this.state.subtitle}>Welcome To The React Version Of The About Page.</h4>
                  </div>
                </div>
              <div  className="container">
                <div className="custom-breadcrumns border-bottom">
                  <div className="container">
                    <a href="#">Home</a>
                    <span className="mx-3 icon-keyboard_arrow_right"></span>
                    <span className="current">About Us</span>
                  </div>
                </div>

                <div className="container pt-5 mb-5">
                  <div className="row">
                    <div className="col-lg-4">
                      <h2 className="section-title-underline">
                        <span>Academics History</span>
                      </h2>
                    </div>
                    <div className="col-lg-4">
                      <p>Lorem ipsum dolor sit amet, consectetur adipisicing elit. Ut, iure dolorum! Nam veniam tempore tenetur aliquam architecto, hic alias quia quisquam, obcaecati laborum dolores. Ex libero cumque veritatis numquam placeat?</p>
                    </div>
                    <div className="col-lg-4">
                      <p>Nam veniam tempore tenetur aliquam
                      architecto, hic alias quia quisquam, obcaecati laborum dolores. Ex libero cumque veritatis numquam placeat?</p>
                    </div>
                  </div>
                </div>
                <Fragment>
                    <About_card image={card_data[0].image} heading={card_data[0].heading} textarea={card_data[0].textarea}/>
                    <About_card image={card_data[1].image} heading={card_data[1].heading} textarea={card_data[1].textarea}/>
                    <About_card image={card_data[2].image} heading={card_data[2].heading} textarea={card_data[2].textarea}/>
                </Fragment>
                <div className="col-md-12" style={{textAlign:"center", color:"black"}}>
                    <h1>Our Teachers</h1>
                </div>
                <div className="col-md-12 mt-3 mb-5" style={{textAlign:"center", color:"black"}}>
                    <Fragment>
                      <TeachersContainer teachers={this.state.teachers.data}/>
                    </Fragment>
                </div>
              </div>
          </div>
            
        )
    }
}

export default Content
