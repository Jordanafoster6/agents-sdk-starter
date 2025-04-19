// backend/src/routes/agent.ts

import express from 'express';
import axios from 'axios';
import { AgentRequest, AgentResponse, agentRequestSchema } from '@shared/types';
import { getContext, saveContext } from '../contextStore';

const router = express.Router();

router.post('/', async (req, res) => {
  const parseResult = agentRequestSchema.safeParse(req.body);

  if (!parseResult.success) {
    return res.status(400).json({ error: parseResult.error.flatten() });
  }

  const { input, sessionId, context: clientContext } = parseResult.data;

  // Load stored context or use one from frontend
  const context = clientContext ?? getContext(sessionId);

  try {
    const response = await axios.post<AgentResponse>(
      'http://localhost:5100/agent',
      { input, context }
    );

    // Save updated context for the session
    saveContext(sessionId, response.data.context ?? {});

    return res.json({
      messages: response.data.messages,
      context: response.data.context,
    });
  } catch (err: any) {
    console.error('🔥 Error talking to agent service:', err.message);
    return res.status(500).json({ error: 'Failed to talk to agent service' });
  }
});

export default router;
