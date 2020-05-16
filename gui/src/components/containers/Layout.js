import React from 'react';
import { Layout, Menu, Breadcrumb } from 'antd';
const { Header, Content, Footer } = Layout;

class CustomProps extends React.Component{

    // state = { source: null };

    // componentDidMount() {
    //     axios
    //     .get(
    //         'https://www.example.com/image.png',
    //         { responseType: 'arraybuffer' },
    //     )
    //     .then(response => {
    //         const base64 = btoa(
    //         new Uint8Array(response.data).reduce(
    //             (data, byte) => data + String.fromCharCode(byte),
    //             '',
    //         ),
    //         );
    //         this.setState({ source: "data:;base64," + base64 });
    //     });
    // }

    render(){
        return(
            <Layout className="layout">
                <Header>
                <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['1']}>
                    <Menu.Item key="1">Home</Menu.Item>
                    <Menu.Item key="2">My Profile</Menu.Item>
                    <Menu.Item key="3">About Us</Menu.Item>
                    <Menu.Item key="4">Courses</Menu.Item>
                    <Menu.Item key="5">Contact</Menu.Item>
                </Menu>
                </Header>
                <Content style={{ padding: '0 50px' }}>
                <Breadcrumb style={{ margin: '16px 0' }}>
                    <Breadcrumb.Item>Home</Breadcrumb.Item>
                    <Breadcrumb.Item>List</Breadcrumb.Item>
                    <Breadcrumb.Item>App</Breadcrumb.Item>
                </Breadcrumb>
                <div className="site-layout-content">
                    {this.props.children}
                </div>
                </Content>
                <Footer style={{ textAlign: 'center' }}>Ant Design ©2018 Created by Ant UED</Footer>
            </Layout>
    
        );
    }
    
}

export default CustomProps;