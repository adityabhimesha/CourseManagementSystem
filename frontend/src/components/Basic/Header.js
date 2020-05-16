import React, { Component } from 'react'

export class Header extends Component {
    
    render() {
        return (
            <div>
                <div className="site-wrap">
                    <div className="py-2 bg-light">
                        <div className="container">
                            <div className="row align-items-center">
                                <div className="col-lg-10 d-none d-lg-block">
                                    <a href="/contact/" className="small mr-3"><span className="icon-question-circle-o mr-2"></span> Have a question?</a>
                                    <a href="#" className="small mr-3"><span className="icon-phone2 mr-2"></span> 10 20 123 456</a>
                                    <a href="mailto:aditya.bhimesha456@gmail.com" className="small mr-3"><span className="icon-envelope-o mr-2"></span> info@academics.com</a>
                                </div>
                            </div>
                        </div>
                    </div>

                    <header className="site-navbar py-4 js-sticky-header site-navbar-target" role="banner">

                    <div className="container">
                    <div className="d-flex align-items-center">
                        <div className="site-logo">
                            <a href="/home/" className="d-block">
                                <img src={"/static/images/logo.png"} alt="Image" className="img-fluid"/>
                            </a>
                        </div>
                        <div className="mr-auto">
                            <nav className="site-navigation position-relative text-right" role="navigation">
                                <ul className="site-menu main-menu js-clone-nav mr-auto d-none d-lg-block">
                                    <li>
                                            <a href="/home/" className="nav-link text-left">Home</a>
                                    </li>
                                    <li>
                                            <a href="/about/" className="nav-link text-left">About Us</a>
                                    </li>
                                    <li>
                                            <a href="" className="nav-link text-left">Courses</a>
                                    </li>
                                    <li>
                                            <a href="/contact/" className="nav-link text-left">Contact</a>
                                    </li>
                                </ul>
                            </nav>

                        </div>
                        <div className="ml-auto">
                            <div className="social-wrap">
                                
                                <a href="#"><span className="icon-facebook"></span></a>
                                <a href="#"><span className="icon-twitter"></span></a>
                                <a href="#"><span className="icon-linkedin"></span></a>

                                <a href="#" className="d-inline-block d-lg-none site-menu-toggle js-menu-toggle text-black"><span
                    className="icon-menu h3"></span></a>
                            </div>
                        </div>

                    </div>
                    </div>

                    </header>
               </div>
            </div>
        )
    }
}

export default Header;
