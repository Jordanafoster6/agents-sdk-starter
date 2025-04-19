import { z } from 'zod';

// Message type sent from or to the agent
export type AgentMessage =
  | {
      type: "chat"; // Standard text message
      role: "user" | "assistant";
      content: string;
    }
  | {
      type: "design"; // Design-related message (for future image generation support)
      role: "user" | "assistant";
      message: string;
      imageUrl: string;
    };

// Stores dynamic context across messages — e.g., selections, preferences, memory
export type ChatContext = Record<string, any>;

// Input sent from frontend to backend
export interface AgentRequest {
  input: string;
  sessionId: string;
  context?: ChatContext;
}

export const agentRequestSchema = z.object({
  input: z.string(),
  sessionId: z.string(),
  context: z.record(z.any()).optional(),
});

// Output sent from backend to frontend
export interface AgentResponse {
  messages: AgentMessage[];
  context?: ChatContext;
}
