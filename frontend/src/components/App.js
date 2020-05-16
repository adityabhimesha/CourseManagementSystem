import React, { Component ,Fragment} from 'react'
import ReactDOM from 'react-dom';
import {BrowserRouter as Router, Route, Switch, Link, Redirect} from "react-router-dom";
import MainPage from "./pages/MainPage";
import Notfound from "./pages/Notfound";
import Contact from "./pages/Contact";

class App extends Component {

    render() {
        return (
            <Router>
                <Switch>
                    <Route path="/react/about/" component={MainPage}/>
                    <Route path="/react/contact/" component={Contact}/>
                    <Route component={Notfound} />
                </Switch>
            </Router>
        )
    }
}

ReactDOM.render(<App />, document.getElementById('app'));