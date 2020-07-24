import React from 'react';
import './App.css';
import {PageHeader} from 'antd';

const Registration = () => (
    <div className="Registration">
            <PageHeader
            className="site-page-header"
            onBack={() => window.history.back()}
            title="Diet For You"
            />
    </div>
);

export default Registration;
