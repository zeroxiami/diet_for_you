import React from 'react';
import ReactDOM from 'react-dom';
import './App.css';
import {List, Layout, Menu, Typography} from 'antd';
import axios from 'axios';

const {Title} = Typography;
const { Header, Content} = Layout;

async function getRecipes() {
    let recipes = await axios.get("http://localhost:8000/api/Recipes/");
    console.log(recipes);
    ReactDOM.render(
        <div>
            <Layout>
                <Header>
                    <div className="logo" />
                    <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['4']}>
                        <Menu.Item key="1"><a href = "http://localhost:3000">Login</a></Menu.Item>
                        <Menu.Item key="2"><a href = "http://localhost:3000/registration">Registration</a></Menu.Item>
                        <Menu.Item key="3"><a href = "http://localhost:3000/info">Personal Info</a></Menu.Item>
                        <Menu.Item key="4"><a href = "http://localhost:3000/recipes">Recipes</a></Menu.Item>
                    </Menu>
                </Header>
                <Content>
                <List
                    dataSource={recipes.data}
                    renderItem={item => (
                        <List.Item>
                            <List.Item.Meta
                             title={<p>User: {item.user}, Total Calories: {item.totalCal} </p>}
                            description={<p>{item.foodItem1}:{item.cal1} cal, 
                            {item.foodItem2}:{item.cal2} cal, 
                            {item.foodItem3}:{item.cal3} cal, 
                            {item.foodItem4}:{item.cal4} cal, 
                            {item.foodItem5}:{item.cal5} cal</p>}
                            />
                        </List.Item>
                      )}

                />
                </Content>
            </Layout>
        </div>, document.getElementById('root')   
    );
}
const Recipes = () => {
    getRecipes();
    return null;
}

export default Recipes;
