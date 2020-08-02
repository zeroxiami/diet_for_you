import React from 'react';
import ReactDOM from 'react-dom';
import {Link} from 'react-router-dom';
import './App.css';
import {PageHeader, Layout, Menu, Typography, Form, Input, InputNumber, Button} from 'antd';
import axios from 'axios';

const {Title} = Typography;
const { Header, Content, Footer } = Layout;

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

async function handlePressEnter(input) {
    const userInput = input.target.value;
    let userData = await axios.get("/api/Info/" + userInput);
    console.log(userData);
    let dataList = [];
    let i = '';
    for (i in userData.data) {
        dataList.push(userData.data[i]);
    }

    const onFinish = values => {
        let updatedItem = {
            "age": values.data.age,
            "calories": values.data.calories,
            "dailyExtraConsume": values.data.dailyExtraConsume,
            "height": values.data.height,
            "id": values.data.id,
            "name": values.data.name,
            "specialDiet": values.data.specialDiet,
            "weight": values.data.weight
        }
        axios.put("http://localhost:8000/api/Info/" + dataList[0] + "/", updatedItem);
    };
    ReactDOM.render(
        <div>
            <Layout>
             <PageHeader
                className="site-page-header"
                onBack={() => window.location.reload(true)}
                title="Diet For You"
            />
            <Content>
                <Title level={2}>Personal Information</Title>
                    <Form {...layout} name="nest-messages" onFinish={onFinish} style={{width: '75%'}} validateMessages={validateMessages}>
                        <Form.Item name={['data', 'id']} label="id" rules={[{ type: 'number', min: 0, max: 9999}]}>
                            <InputNumber placeholder={dataList[0]}/>
                        </Form.Item>
                        <Form.Item name={['data', 'calories']} label="Calories" rules={[{ type: 'number', min: 0, max: 9999}]}>
                            <InputNumber placeholder={dataList[1]}/>
                        </Form.Item>
                        <Form.Item name={['data', 'height']} label="Height" rules={[{ type: 'number', min: 0, max: 999 }]}>
                            <InputNumber placeholder={dataList[2]}/>
                        </Form.Item>
                        <Form.Item name={['data', 'weight']} label="Weight" rules={[{ type: 'number', min: 0, max: 999 }]}>
                            <InputNumber placeholder={dataList[3]}/>
                        </Form.Item>
                        <Form.Item name={['data', 'name']} label="Name">
                            <Input placeholder={dataList[4]}/>
                        </Form.Item>
                        <Form.Item name={['data', 'dailyExtraConsume']} label="DailyExtraConsume" rules={[{ type: 'number', min: 0, max: 9999}]}>
                            <InputNumber placeholder={dataList[5]}/>
                        </Form.Item>
                        <Form.Item name={['data', 'specialDiet']} label="SpecialDiet">
                            <Input placeholder={dataList[6]}/>
                        </Form.Item>
                        <Form.Item name={['data', 'age']} label="Age" rules={[{ type: 'number', min: 0, max: 99}]}>
                            <InputNumber placeholder={dataList[7]}/>
                        </Form.Item>
                        <Form.Item wrapperCol={{ ...layout.wrapperCol, offset: 8 }}>
                            <Button type="primary" htmlType="submit">
                                Submit
                            </Button>
                        </Form.Item>
                    </Form>
                </Content>
            </Layout>
        </div>, document.getElementById('root')
    );
}

const Info = () => {
    return(
    <div className="Info">
        <Layout>
            <Header>
                <div className="logo" />
                <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['3']}>
                <Menu.Item key="1"><Link to="/">Login</Link></Menu.Item>
                    <Menu.Item key="2"><Link to="/registration">Registration</Link></Menu.Item>
                    <Menu.Item key="3"><Link to="/info">Personal Info</Link></Menu.Item>
                    <Menu.Item key="4"><Link to="/recipes">Recipes</Link></Menu.Item>
                </Menu>
            </Header>
            <Content className="info-content">
                <br></br>
                <Title level={2}>Enter your UserID here to view or update your personal information.</Title>
                <Input
                    placeholder="Enter your userID" 
                    style={{width: '25%'}}
                    onPressEnter={handlePressEnter}
                />
            </Content>
            <Footer></Footer>
        </Layout>
    </div>
    );
}   

export default Info;
