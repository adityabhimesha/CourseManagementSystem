import React, { Component } from 'react'

export class Notfound extends Component {
    render() {
        return (
            <div className="row text-center text-dark" style={{marginTop:"10%"}}>
                <div className="col-md-12">
                    <img width="100px" height="100px" src="https://hotemoji.com/images/dl/9/white-frowning-face-emoji-by-twitter.png"/>
                </div>
                <div className="col-md-12 mt-4">
                    <h2>404, Page Not Found :(</h2>
                </div>
            </div>
        )
    }
}

export default Notfound;
