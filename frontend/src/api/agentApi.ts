import axios from "axios";

const api = axios.create({
  baseURL:
    "http://localhost:8000/api",
});

export const runAgent =
  async (payload: any) => {

    const response =
      await api.post(
        "/run-agent",
        payload
      );

    return response.data;
  };

export const getResult =
  async (runId: string) => {

    const response =
      await api.get(
        `/results/${runId}`
      );

    return response.data;
  };

export const getRuns =
  async () => {

    const response =
      await api.get("/runs");

    return response.data;
  };

export default api;