export const getAuthHeader = (): Record<string, string> | undefined => {
  const token = localStorage.getItem("token");
  return token ? { Authorization: `Bearer ${token}` } : undefined;
};