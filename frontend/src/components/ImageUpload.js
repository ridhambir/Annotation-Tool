import React, { useState } from 'react';
import axios from 'axios';

const ImageUpload = () => {
  const [file, setFile] = useState(null);
  const [preview, setPreview] = useState(null);
  const [uploading, setUploading] = useState(false);
  const [result, setResult] = useState(null);
  const [error, setError] = useState(null);

  const handleFileChange = (event) => {
    const selectedFile = event.target.files[0];
    if (selectedFile) {
      setFile(selectedFile);
      const reader = new FileReader();
      reader.onloadend = () => {
        setPreview(reader.result);
      };
      reader.readAsDataURL(selectedFile);
      setError(null);
    }
  };

  const handleSubmit = async (event) => {
    event.preventDefault();
    
    if (!file) {
      setError('Please select an image first');
      return;
    }

    const formData = new FormData();
    formData.append('file', file);

    setUploading(true);
    try {
      const response = await axios.post('http://localhost:5000/upload', formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
      });
      setResult(response.data);
      setError(null);
    } catch (err) {
      setError(err.response?.data?.error || 'Upload failed. Make sure the backend is running.');
      setResult(null);
    } finally {
      setUploading(false);
    }
  };

  return (
    <div className="upload-section">
      <div className="upload-container">
        <h1>Image Upload</h1>

        <div className="upload-content">
          <div className="form-column">
            <form onSubmit={handleSubmit} className="upload-form">
              <div className="file-input-wrapper">
                <input
                  type="file"
                  accept="image/*"
                  onChange={handleFileChange}
                  id="file-input"
                  disabled={uploading}
                />
                <label htmlFor="file-input" className="file-label">
                  {preview ? 'Change Image' : 'Choose Image'}
                </label>
              </div>

              {preview && (
                <div className="preview-section">
                  <p>Preview:</p>
                  <img src={preview} alt="preview" className="preview-image" />
                </div>
              )}

              <button type="submit" className="submit-btn" disabled={uploading || !file}>
                {uploading ? 'Uploading...' : 'Upload & Process'}
              </button>
            </form>

            {error && <div className="error-message">{error}</div>}
          </div>

          <div className="result-column">
            <div className="result-section">
              <h2>Processing Result</h2>
              {!result && <p className="placeholder">No result yet — upload an image to see the output here.</p>}
              {result && (
                <>
                  {result.annotated && result.annotated.length > 0 ? (
                    <div className="result-content">
                      <p>Annotated (Detected):</p>
                      <img src={result.annotated[0]} alt="annotated" className="result-image" />
                    </div>
                  ) : result.image_url && (
                    <div className="result-content">
                      <p>Processed Image:</p>
                      <img src={result.image_url} alt="result" className="result-image" />
                    </div>
                  )}
                  {result.message && <p className="result-message">{result.message}</p>}
                  {result.prediction !== undefined && (
                    <div className="prediction-result">
                      <p><strong>Prediction:</strong> {String(result.prediction)}</p>
                      {result.confidence && <p><strong>Confidence:</strong> {result.confidence}</p>}
                    </div>
                  )}
                </>
              )}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default ImageUpload;
