import React from 'react';
import { BrowserRouter as Router, Route, Switch } from 'react-router-dom';
import Portfolio from './components/Portfolio';
import Skills from './components/Skills';
import ContactForm from './components/ContactForm';

const App = () => {
  return (
    <Router>
      <Switch>
        <Route path='/' exact component={Portfolio} />
        <Route path='/skills' component={Skills} />
        <Route path='/contact' component={ContactForm} />
      </Switch>
    </Router>
  );
};

export default App;