const initialState = [];

const skillsReducer = (state = initialState, action) => {
  switch (action.type) {
    case 'SET_SKILLS':
      return action.payload;
    default:
      return state;
  }
};

export default skillsReducer;