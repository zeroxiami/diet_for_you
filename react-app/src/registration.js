import React from 'react';
import {Link} from 'react-router-dom';
import './App.css';
import {Layout, Menu, Form, Input, Button, Typography, InputNumber} from 'antd';
import axios from 'axios';

const {Header, Content, Footer } = Layout;
const {Title} = Typography;

const layout = {
    labelCol: { span: 8 },
    wrapperCol: { span: 16 },
  };
  
  const validateMessages = {
    required: '${label} is required!',
    types: {
      email: '${label} is not validate email!',
      number: '${label} is not a validate number!',
    },
    number: {
      range: '${label} must be between ${min} and ${max}',
    },
  };

const Registration = () => {
    async function onFinish(values) {
        let list = await axios.get("/api/Info");
        let i = '';
        let id_nums = [];
        for (i in list.data) {
            id_nums.push(parseInt(list.data[i].id, 10));
        }
        let new_id = Math.max.apply(null, id_nums) + 1;
        console.log(new_id);
        let updatedItem = {
            "age": values.data.age,
            "calories": values.data.calories,
            "dailyExtraConsume": values.data.dailyExtraConsume,
            "height": values.data.height,
            "id": new_id,
            "name": values.data.name,
            "specialDiet": values.data.specialDiet,
            "weight": values.data.weight
        }
        axios.post("http://localhost:8000/api/Info/", updatedItem);
      };
    return(
        <div className="Registration">
            <Layout>
                <Header>
                    <div className="logo" />
                    <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['2']}>
                        <Menu.Item key="1"><Link to="/">Login</Link></Menu.Item>
                        <Menu.Item key="2"><Link to="/registration">Registration</Link></Menu.Item>
                        <Menu.Item key="3"><Link to="/info">Personal Info</Link></Menu.Item>
                        <Menu.Item key="4"><Link to="/recipes">Recipes</Link></Menu.Item>
                    </Menu>
                </Header>
                <Content>
                    <br></br>
                    <Title level={2}>Please enter your information to register for an account.</Title>
                    <Form {...layout} name="nest-messages" onFinish={onFinish} style={{width: '75%'}} validateMessages={validateMessages}>
                        <Form.Item name={['user', 'name']} label="Username">
                            <Input placeholder=""/>
                        </Form.Item>
                        <Form.Item
                        label="Password"
                        name="password"
                        rules={[{message: 'Please input your password!' }]}
                        >
                            <Input.Password />
                        </Form.Item>
                        <Form.Item name={['data', 'calories']} label="Calories" rules={[{ type: 'number', min: 0, max: 9999}]}>
                            <InputNumber />
                        </Form.Item>
                        <Form.Item name={['data', 'height']} label="Height" rules={[{ type: 'number', min: 0, max: 999 }]}>
                            <InputNumber />
                        </Form.Item>
                        <Form.Item name={['data', 'weight']} label="Weight" rules={[{ type: 'number', min: 0, max: 999 }]}>
                            <InputNumber />
                        </Form.Item>
                        <Form.Item name={['data', 'name']} label="Name">
                            <Input />
                        </Form.Item>
                        <Form.Item name={['data', 'dailyExtraConsume']} label="DailyExtraConsume" rules={[{ type: 'number', min: 0, max: 9999}]}>
                            <InputNumber />
                        </Form.Item>
                        <Form.Item name={['data', 'specialDiet']} label="SpecialDiet">
                            <Input />
                        </Form.Item>
                        <Form.Item name={['data', 'age']} label="Age" rules={[{ type: 'number', min: 0, max: 99}]}>
                            <InputNumber />
                        </Form.Item>
                        <Form.Item wrapperCol={{ ...layout.wrapperCol, offset: 8 }}>
                            <Button type="primary" htmlType="submit">
                                Submit
                            </Button>
                        </Form.Item>
                    </Form>
                </Content>
                <Footer></Footer>
            </Layout>
        </div>
    );
}  

export default Registration;
