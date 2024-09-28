// Secret key for JWT token
const crypto = require('crypto');

module.exports = {
  JWT_SECRET: crypto.randomBytes(32).toString('hex'),
  // might be useful in the future
  DISABLED_OPERATION_MONGO: [
    "$listLocalSessions",
    "$listSessions",
    "$listSearchIndexes",
    "$listSampledQueries",
    "$indexStats",
    "$limit",
    "$documents",
    "$regex",
    "$func",
    "$lookup",
    "$where",
    "$currentOp",
    "$changeStream",
    "$vectorSearch",
    "$unwind",
    "$unset",
    "$setWindowFields",
    "$search",
    "$searchMeta",
    "$queryStats",
    "$planCacheStats",
    "$collStats",
    "$graphLookup",
    "$replaceRoot",
    "$mergeObjects",
    "$setUnion",
    "$setIntersection",
    "$meta",
    "$zip",
    "$unionWith",
    "$match",
    "$out",
    "$merge",
    "$accumulator",
    "$function",
    "$set"
  ]
};
