import React from 'react';
import { Route, Link, BrowserRouter as Router } from 'react-router-dom';
import {Switch} from 'react-router-dom';
import {withRouter} from 'react-router';
import './App.css';
import {Space, Layout, Menu, Typography, Form, Input, Button} from 'antd';
import Registration from './registration';
import Info from './info';
import Recipes from './recipes';

const { Header, Content, Footer } = Layout;
const {Title} = Typography;

const layout = {
  labelCol: { span: 8 },
  wrapperCol: { span: 16 },
};
const tailLayout = {
  wrapperCol: { offset: 8, span: 16 },
};

const App = () => (
  <Router>
    <Switch>
    <Route exact path="/" component={Home} />
    <Route exact path="/registration" component={withRouter(Registration)} />
    <Route exact path="/info" component={withRouter(Info)} />
    <Route exact path="/recipes" component={withRouter(Recipes)} />
    </Switch>
  </Router>
);

const Home = () => {
  const onFinish = values => {
    console.log('Success:', values);
  };

  const onFinishFailed = errorInfo => {
    console.log('Failed:', errorInfo);
  };

  return(
    <div className="App">
      <Layout>
        <Header>
          <div className="logo" />
            <Menu theme="dark" mode="horizontal" defaultSelectedKeys={['1']}>
              <Menu.Item key="1"><Link to="/">Login</Link></Menu.Item>
              <Menu.Item key="2"><Link to="/registration">Registration</Link></Menu.Item>
              <Menu.Item key="3"><Link to="/info">Personal Info</Link></Menu.Item>
              <Menu.Item key="4"><Link to="/recipes">Recipes</Link></Menu.Item>
            </Menu>
        </Header>
        <Content>
          <br></br>
          <Title level={2}>Login to your account or register for a new one.</Title>
          <Form
          {...layout}
          name="basic"
          initialValues={{ remember: true }}
          onFinish={onFinish}
          onFinishFailed={onFinishFailed}
          style={{width: '75%'}}
        >
          <Form.Item
            label="Username"
            name="username"
            rules={[{ required: true, message: 'Please input your username!' }]}
          >
            <Input />
          </Form.Item>

          <Form.Item
            label="Password"
            name="password"
            rules={[{ required: true, message: 'Please input your password!' }]}
          >
            <Input.Password />
          </Form.Item>
          <Form.Item {...tailLayout}>
            <Button type="primary" htmlType="submit">
              Login
            </Button>
          </Form.Item>
        </Form>
      </Content>
      <Footer></Footer>
    </Layout>
  </div>
  );
};

export default App;
