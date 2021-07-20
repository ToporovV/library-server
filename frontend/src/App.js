import React from 'react';
import logo from './logo.svg';
import './App.css';
import UserList from './components/users.js';

class App extends React.Component {
    constructor(props) {
        super(props);
        this.state = {'users': []};
    };

    componentDidMount() {
        this.setState({'users': users})
    }

    render() {
        return (<div>
            <UserList users={this.state.users} />
        </div>)
    };

};

export default App;
