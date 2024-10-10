{
  "backend": "from flask import Flask, jsonify, request\n\napp = Flask(__name__)\n\n@app.route('/api/data', methods=['GET'])\ndef get_data():\n    return jsonify({'message': 'Hello, World!'})\n\nif __name__ == '__main__':\n    app.run(debug=True, port=5000)\n",
  "frontend": "import React, { useEffect, useState } from 'react';\n\nconst App = () => {\n  const [data, setData] = useState(null);\n\n  useEffect(() => {\n    const fetchData = async () => {\n      const response = await fetch('/api/data');\n      const result = await response.json();\n      setData(result.message);\n    };\n    fetchData();\n  }, []);\n\n  return (\n    <div>\n      <h1>User Interface</h1>\n      <p>{data}</p>\n    </div>\n  );\n};\n\nexport default App;\n",
  "dependencies": {
    "backend": ["Flask"],
    "frontend": ["react", "react-dom"]
  },
  "build_command": "npm run build",
  "start_command": "flask run"
}