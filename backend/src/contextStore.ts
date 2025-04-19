// backend/src/contextStore.ts

// Simple in-memory store to hold per-session context across user messages
const store: Record<string, Record<string, any>> = {};

// Retrieve context for a given session
export function getContext(sessionId: string): Record<string, any> {
  return store[sessionId] || {};
}

// Save updated context for a given session
export function saveContext(sessionId: string, context: Record<string, any>) {
  store[sessionId] = context;
}
