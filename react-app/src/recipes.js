import React from 'react';
import ReactDOM from 'react-dom';
import {Link} from 'react-router-dom';
import './App.css';
import {List, Layout, Menu, Form, Input, Button, Typography, InputNumber} from 'antd';
import axios from 'axios';

const {Title} = Typography;
const { Header, Content} = Layout;

async function getRecipes() {
    let recipes = await axios.get("http://localhost:8000/api/Recipes");
    ReactDOM.render(
        <div>
            <Layout>
                <Header>
                </Header>
                <Content>
                <List
                    dataSource={recipes}
                    renderItem={item => (
                        <List.Item>
                            {item.User}
                            {item.FoodItem1}
                            {item.Cal1}
                            {item.FoodItem2}
                            {item.Cal2}
                            {item.FoodItem3}
                            {item.Cal3}
                        </List.Item>
                      )}

                />
                </Content>
            </Layout>
        </div>, document.getElementById('root')   
    );
}
const Recipes = () => {
    return(
        <Layout>
                <Header>
                    <div className="logo" />
                    <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['4']}>
                        <Menu.Item key="1"><Link to="/">Login</Link></Menu.Item>
                        <Menu.Item key="2"><Link to="/registration">Registration</Link></Menu.Item>
                        <Menu.Item key="3"><Link to="/info">Personal Info</Link></Menu.Item>
                        <Menu.Item key="4"><Link to="/recipes">Recipes</Link></Menu.Item>
                    </Menu>
                </Header>
                <Content>
                    <Button type="primary" onClick={getRecipes}>Load Recipes</Button>
                </Content>
            </Layout>
    );
}

export default Recipes;
