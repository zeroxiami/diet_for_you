import React from 'react';
import './App.css';
import {PageHeader, Typography, Form, Input, InputNumber, Button, DatePicker} from 'antd';

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

const Info = () => {
    const onFinish = values => {
        console.log(values);
      };
    return(
    <div className="Registration">
        <PageHeader
            className="site-page-header"
            onBack={() => window.history.back()}
            title="Diet For You"
        />
    <Title level={2}>Personal Information.</Title>
    <Form {...layout} name="nest-messages" onFinish={onFinish} style={{width: '75%'}} validateMessages={validateMessages}>
        <Form.Item label="UserID"></Form.Item>
        <Form.Item name={['user', 'name']} label="Name">
            <Input placeholder="User Name"/>
        </Form.Item>
        <Form.Item name={['user', 'age']} label="Age" rules={[{ type: 'number', min: 0, max: 99 }]}>
            <InputNumber placeholder="User Age"/>
        </Form.Item>
        <Form.Item name={['user', 'weight']} label="Weight" rules={[{ type: 'number', min: 0, max: 999 }]}>
            <InputNumber placeholder="User Weight"/>
        </Form.Item>
        <Form.Item name={['user', 'goals']} label="Goals">
            <Input placeholder="User Goals"/>
        </Form.Item>
        <Form.Item label="Date Joined">
          <DatePicker placeholder=""/>
        </Form.Item>
        <Form.Item name={['user', 'eating_style']} label="Eating Style">
            <Input placeholder="User Eating Style"/>
        </Form.Item>
        <Form.Item name={['user', 'daily_exercise']} label="Daily Exercise">
            <Input placeholder="User Exercise"/>
        </Form.Item>
        <Form.Item name={['user', 'dietary_restriction']} label="Dietary Restriction">
            <Input placeholder="User Dietary Restrictions"/>
        </Form.Item>
        <Form.Item wrapperCol={{ ...layout.wrapperCol, offset: 8 }}>
            <Button type="primary" htmlType="submit">
            Submit
            </Button>
        </Form.Item>
    </Form>
    </div>
    );
}   

export default Info;
