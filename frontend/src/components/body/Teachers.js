import React, { Component } from 'react'


class Teachers extends React.Component {   
    render() {
        return (
                <div className="col-lg-4 col-md-6 mt-5 mb-5 mb-lg-5">
                    <div className="feature-1 border person text-center">
                        <img src={this.props.profile_pic} alt="Image" className="img-fluid"/>
                    <div className="feature-1-content">
                        <span className="position mb-3 d-block">{ this.props.category }</span>    
                        <p>Number of Courses Available:{ this.props.courses }</p>
                        <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit morbi hendrerit elit</p>
                    </div>
                    </div>
                </div>
        );
    }
}


class TeachersContainer extends React.Component {   
    render() {
        var arr = this.props.teachers;
        console.log(this.props.teachers);
        var elements=[];
        for(var i=0;i<arr.length;i++){
            elements.push(<Teachers 
                category={arr[i].category} 
                courses={arr[i].num_of_courses} 
                profile_pic={arr[i].profile_pic} 
                age={arr[i].age} 
                key={i}

                />);
        }
        return (
            <div className="row mt-5"> 
            {elements}
            </div>
        );
    }
}
export default TeachersContainer;