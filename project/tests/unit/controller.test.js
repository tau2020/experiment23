const controller = require('../src/controller');
const mockRequest = (body) => ({ body });
const mockResponse = () => {
  const res = {};
  res.json = jest.fn().mockReturnValue(res);
  res.status = jest.fn().mockReturnValue(res);
  return res;
};

describe('Controller Functions', () => {
  it('should handle the request correctly', () => {
    const req = mockRequest({ key: 'value' });
    const res = mockResponse();
    controller.handleRequest(req, res);
    expect(res.status).toHaveBeenCalledWith(200);
    expect(res.json).toHaveBeenCalledWith({ success: true });
  });
});