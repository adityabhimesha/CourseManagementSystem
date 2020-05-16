import React, { Component ,Fragment} from 'react';
import Header from '../Basic/Header';
import Footer from '../Basic/Footer';
import Form from '../body/Form';

class Contact extends Component {

    render() {
        return (
            <Fragment>
                <Header/>
                <Form />
                <Footer/>
            </Fragment>
        )
    }
}

export default Contact;