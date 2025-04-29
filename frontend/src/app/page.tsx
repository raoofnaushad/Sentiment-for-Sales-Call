// src/app/page.tsx
'use client';

import { useState } from 'react';
import Image from 'next/image';

export default function Home() {
  const [isAnalyzing, setIsAnalyzing] = useState(false);
  const [result, setResult] = useState<{
    sentiment: string;
    confidence: number;
  } | null>(null);

  const analyzeSentiment = async (text: string) => {
    setIsAnalyzing(true);
    try {
      const response = await fetch('/api/analyze-sentiment', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text }),
      });
      const data = await response.json();
      setResult(data);
    } catch (error) {
      console.error('Error analyzing sentiment:', error);
    } finally {
      setIsAnalyzing(false);
    }
  };

  return (
    <main className="min-h-screen bg-white">
      {/* Hero Section */}
      <div className="bg-gray-900 p-4">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
        <svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 80 70" width="80" height="70" fill="white">
  <path d="M13.6 61.2H3V8.9h9.6v52.3zM33.6 64.2H16.1V6h16.5v58.2zM67.7 66h-31V3h31v63z" />
</svg>
        </div>
      </div>

      {/* Hero Section - Modified with darker text */}
      <div className="bg-gray-50">
        <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
          <div className="grid grid-cols-1 lg:grid-cols-3 gap-8 items-center">
            <div className="lg:col-span-2 text-left">
              <h1 className="text-4xl tracking-tight font-extrabold text-gray-900 sm:text-5xl md:text-6xl">
                <span className="block text-gray-900">Alert Driving</span>
                <span className="block text-blue-700">Sentiment Analysis</span>
              </h1>
              <p className="mt-3 text-base text-gray-700 sm:text-lg md:mt-5 md:text-xl md:max-w-3xl">
                Enhance your sales performance with real-time sentiment analysis. Understand customer emotions and improve your communication strategy.
              </p>
            </div>
            <div className="relative h-[400px] w-full">
              <Image
                src="/AlertDrivingImage.avif"
                alt="AlertDriving Dashboard"
                fill
                style={{ objectFit: 'contain' }}
                priority
              />
            </div>
          </div>
        </div>
      </div>

      {/* Analysis Section */}
      <div className="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 py-12">
        <div className="bg-white rounded-xl shadow-2xl overflow-hidden">
          <div className="p-6 md:p-8">
            <div className="mb-6">
              <h2 className="text-2xl font-bold text-gray-900">Analyze Your Sales Call</h2>
              <p className="mt-2 text-gray-700">Paste your sales call transcript below to get instant sentiment analysis</p>
            </div>
            
            <textarea
              className="w-full h-48 p-4 bg-gray-50 border border-gray-200 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent transition duration-200 text-gray-900"
              placeholder="Paste your sales call transcript here..."
              onChange={(e) => {
                if (e.target.value.trim()) {
                  analyzeSentiment(e.target.value);
                } else {
                  setResult(null);
                }
              }}
            />

            {isAnalyzing && (
              <div className="mt-6 flex justify-center">
                <div className="inline-block animate-spin rounded-full h-8 w-8 border-4 border-blue-500 border-t-transparent"></div>
              </div>
            )}

            {result && (
              <div className="mt-8">
                <div className="bg-gray-50 rounded-lg p-6">
                  <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
                    <div className="bg-white rounded-lg p-6 shadow-md">
                      <h3 className="text-lg font-semibold text-gray-700 mb-2">Sentiment</h3>
                      <div className={`text-3xl font-bold ${
                        result.sentiment === 'Positive' ? 'text-green-600' :
                        result.sentiment === 'Negative' ? 'text-red-600' :
                        'text-yellow-600'
                      }`}>
                        {result.sentiment}
                      </div>
                    </div>
                    
                    <div className="bg-white rounded-lg p-6 shadow-md">
                      <h3 className="text-lg font-semibold text-gray-700 mb-2">Confidence</h3>
                      <div className="relative">
                        <div className="flex items-center justify-between mb-2">
                          <div className="text-3xl font-bold text-blue-600">
                            {Math.round(result.confidence * 100)}%
                          </div>
                        </div>
                        <div className="h-3 relative max-w-xl rounded-full overflow-hidden">
                          <div className="w-full h-full bg-gray-200 absolute"></div>
                          <div
                            className="h-full bg-blue-500 absolute transition-all duration-500 ease-out"
                            style={{ width: `${result.confidence * 100}%` }}
                          ></div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
            )}
          </div>
        </div>

        {/* Features Section */}
        <div className="mt-16 grid grid-cols-1 md:grid-cols-3 gap-8">
          <div className="bg-white p-6 rounded-lg shadow-md">
            <div className="text-blue-600 text-2xl mb-4">🎯</div>
            <h3 className="text-xl font-semibold mb-2 text-gray-900">Instant Analysis</h3>
            <p className="text-gray-600">Get real-time sentiment analysis of your sales calls with high accuracy.</p>
          </div>
          
          <div className="bg-white p-6 rounded-lg shadow-md">
            <div className="text-blue-600 text-2xl mb-4">📈</div>
            <h3 className="text-xl font-semibold mb-2 text-gray-900">Performance Tracking</h3>
            <p className="text-gray-600">Monitor and improve your sales communication effectiveness.</p>
          </div>
          
          <div className="bg-white p-6 rounded-lg shadow-md">
            <div className="text-blue-600 text-2xl mb-4">🔒</div>
            <h3 className="text-xl font-semibold mb-2 text-gray-900">Secure Analysis</h3>
            <p className="text-gray-600">Your data is processed securely and confidentially.</p>
          </div>
        </div>
      </div>
    </main>
  );
}