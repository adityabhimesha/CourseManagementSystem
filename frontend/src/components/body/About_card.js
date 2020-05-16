import React, { Component } from 'react'

export class About_card extends Component {
    render() {
        return (
            <div className="site-section">
                <div className="container">
                    <div className="row mb-3 mt-3">
                        <div className="col-lg-6 mb-lg-0 mb-4">
                            <img src={this.props.image} alt="Image" className="img-fluid"/> 
                        </div>
                        <div className="col-lg-5 ml-auto align-self-center">
                            <h2 className="section-title-underline mb-2 mt-3">
                                <span>{this.props.heading}</span>
                            </h2>
                            <p>{this.props.textarea}</p>
                        </div>
                    </div>
                </div>
            </div>
        )
    }
}

export default About_card;
