import React, { Component ,Fragment} from 'react';
import Header from '../Basic/Header';
import Footer from '../Basic/Footer';
import Content from '../body/Content';

class MainPage extends Component {

    render() {
        return (
            <Fragment>
                <Header/>
                <Content />
                <Footer/>
            </Fragment>
        )
    }
}

export default MainPage;