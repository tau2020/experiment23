import { combineReducers } from 'redux';
import portfolioReducer from './portfolioReducer';
import skillsReducer from './skillsReducer';

const rootReducer = combineReducers({
  portfolio: portfolioReducer,
  skills: skillsReducer
});

export default rootReducer;