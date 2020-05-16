import React, { Component } from 'react'
export class Footer extends Component {
    
    render() {
        
        var bg_image = {
            backgroundImage: `url(${"/static/images/bg_1.jpg"})`
        }
        return (
            <div>
                <div className="site-section ftco-subscribe-1" style={bg_image}>
                    <div className="container">
                        <div className="row align-items-center px-4">
                            <div className="col-lg-7">
                                <h2>Subscribe to us!</h2>
                                <p>Far far away, behind the word mountains, far from the countries Vokalia and Consonantia,</p>
                            </div>
                            <div className="col-lg-5">
                                <form action="" className="d-flex">
                                    <input type="text" className="rounded form-control mr-2 py-3" placeholder="Enter your email"/>
                                    <button className="btn btn-primary rounded py-3 px-4" type="submit">Send</button>
                                </form>
                            </div>
                        </div>
                    </div>
                </div>

                <div className="footer">
                    <div className="container">
                        <div className="row align-items-center px-4">
                            <div className="col-lg-3">
                                <p className="mb-4"><img src={"/static/images/logo.png"} alt="Image" className="img-fluid"/></p>
                                <p>Lorem ipsum dolor sit amet consectetur adipisicing elit.</p>
                                <p> Beatae nemo minima qui dolor, iusto iure.</p>
                                <p><a href="#">Learn More</a></p>
                            </div>
                            <div className="col-lg-9">
                                <div className="row">
                                    <div className="col-lg-7">
                                        <h3 className="footer-heading"><span>Contact</span></h3>
                                        <a href="/contact/" className="small"><span className="icon-question-circle-o mr-2"></span> Have a question?</a><br/>
                                        <a href="#" className="small"><span className="icon-phone2 mr-2"></span> 10 20 123 456</a><br/>
                                        <a href="mailto:aditya.bhimesha456@gmail.com" className="small"><span className="icon-envelope-o mr-2"></span> info@academics.com</a>
                                    </div>

                                    <div className="col-lg-5">
                                        <h3 className="footer-heading"><span>Help</span></h3>
                                        <ul className="list-unstyled">
                                            <li><a href="#">Help Center</a></li>
                                            <li><a href="#">Support Community</a></li>
                                            <li><a href="#">Press</a></li>
                                            <li><a href="#">Share Your Story</a></li>
                                            <li><a href="#">Our Supporters</a></li>
                                            <li><a href="">Become A Teacher Now!</a></li>
                                        </ul>
                                    </div>
                                </div>
                            </div>
                        </div>
                    </div>
                </div>

            </div>
        )
    }
}

export default Footer
