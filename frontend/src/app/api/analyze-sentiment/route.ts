// src/app/api/analyze-sentiment/route.ts
import { NextResponse } from 'next/server';

// You can store the base URL in an environment variable
// Create a .env.local file in the root of your project with:
// NEXT_PUBLIC_API_URL=http://localhost:8000
const API_URL = process.env.NEXT_PUBLIC_API_URL || 'http://localhost:8000';

export async function POST(request: Request) {
  const { text } = await request.json();

  try {
    const response = await fetch(`${API_URL}/api/sentiment-analysis`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ text }),
    });

    if (!response.ok) {
      throw new Error('Failed to analyze sentiment');
    }

    const result = await response.json();
    return NextResponse.json(result);

  } catch (error) {
    console.error('Error analyzing sentiment:', error);
    return NextResponse.json(
      { error: 'Failed to analyze sentiment' },
      { status: 500 }
    );
  }
}