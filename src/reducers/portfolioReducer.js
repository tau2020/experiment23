const initialState = { items: [] };

const portfolioReducer = (state = initialState, action) => {
  switch (action.type) {
    case 'SET_PORTFOLIO_ITEMS':
      return { ...state, items: action.payload };
    default:
      return state;
  }
};

export default portfolioReducer;